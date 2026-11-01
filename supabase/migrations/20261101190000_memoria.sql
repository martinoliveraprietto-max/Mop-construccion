-- Cerebro MOP (aprobado por Martin el 1-nov-2026, plan en CEREBRO_MOP.md).
-- Nivel tibio de la memoria: una ficha por obra, constructora, proveedor, bot, trámite o proyecto,
-- y los hechos de cada ficha (solo se agregan). Sin políticas: como public.tablero, solo las
-- tareas con Supabase (rol de servicio / execute_sql) las leen y escriben; la clave pública no.

create extension if not exists pg_trgm with schema extensions;
create extension if not exists unaccent with schema extensions;

create table if not exists public.memoria_fichas (
  id bigint generated always as identity primary key,
  tipo text not null check (tipo in ('obra','constructora','proveedor','bot','tramite',
                                     'persona','proyecto','sistema')),
  nombre text not null unique,
  alias text[] not null default '{}',
  resumen text not null default '' check (char_length(resumen) <= 600),
  estado text,
  proximo text,
  vence date,
  fuente text,
  actualizado timestamptz not null default now(),
  busqueda text not null default ''
);

create table if not exists public.memoria_hechos (
  id bigint generated always as identity primary key,
  ficha_id bigint not null references public.memoria_fichas(id) on delete cascade,
  fecha timestamptz not null default now(),
  texto text not null,
  fuente text not null,
  quien text not null
);
create index if not exists memoria_hechos_ficha on public.memoria_hechos (ficha_id, fecha desc);

-- Texto normalizado (minúsculas, sin acentos) para buscar con nombres mal escritos.
create or replace function public.memoria_normal(t text) returns text
language sql immutable set search_path = '' as
$$ select lower(extensions.unaccent('extensions.unaccent'::regdictionary, coalesce(t, ''))) $$;

create or replace function public.memoria_fichas_al_guardar() returns trigger
language plpgsql set search_path = '' as
$$
begin
  new.actualizado := now();
  new.busqueda := public.memoria_normal(new.nombre || ' ' || array_to_string(new.alias, ' ')
                  || ' ' || new.resumen || ' ' || coalesce(new.estado, '') || ' '
                  || coalesce(new.proximo, ''));
  return new;
end
$$;
drop trigger if exists memoria_fichas_guardar on public.memoria_fichas;
create trigger memoria_fichas_guardar before insert or update on public.memoria_fichas
  for each row execute function public.memoria_fichas_al_guardar();

create index if not exists memoria_fichas_trgm on public.memoria_fichas
  using gin (busqueda extensions.gin_trgm_ops);

-- Búsqueda en una sola consulta: fichas parecidas a la pregunta, con sus 5 hechos más nuevos.
create or replace function public.memoria_buscar(q text, cuantos int default 5)
returns table (tipo text, nombre text, resumen text, estado text, proximo text, vence date,
               fuente text, actualizado timestamptz, puntaje real, hechos jsonb)
language sql stable set search_path = '' as
$$
  with p as (select public.memoria_normal(q) as n)
  select f.tipo, f.nombre, f.resumen, f.estado, f.proximo, f.vence, f.fuente, f.actualizado,
         greatest(extensions.word_similarity(p.n, f.busqueda),
                  extensions.similarity(p.n, public.memoria_normal(f.nombre))) as puntaje,
         coalesce((select jsonb_agg(jsonb_build_object('fecha', h.fecha, 'texto', h.texto,
                                                       'fuente', h.fuente, 'quien', h.quien)
                                    order by h.fecha desc)
                   from (select * from public.memoria_hechos h2 where h2.ficha_id = f.id
                         order by h2.fecha desc limit 5) h), '[]'::jsonb) as hechos
  from public.memoria_fichas f, p
  where f.busqueda like '%' || p.n || '%'
     or extensions.word_similarity(p.n, f.busqueda) > 0.35
  order by puntaje desc, f.actualizado desc
  limit cuantos
$$;

alter table public.memoria_fichas enable row level security;
alter table public.memoria_hechos enable row level security;
revoke all on public.memoria_fichas, public.memoria_hechos from anon, authenticated;
revoke execute on function public.memoria_buscar(text, int) from anon, authenticated, public;

comment on table public.memoria_fichas is 'Cerebro MOP, nivel tibio: una ficha por obra, constructora, proveedor, bot, trámite o proyecto. Sin políticas: solo rol de servicio.';
comment on table public.memoria_hechos is 'Cerebro MOP: hechos con fuente y fecha de cada ficha. Solo se agregan.';
