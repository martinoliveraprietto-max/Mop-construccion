-- Tabla "tablero" (pedido de Martin, 19-oct-2026): una fila por número o estado de cada
-- frente del sistema de asistentes (cazador, vigilante, bandeja, guardián…). Cada tarea
-- programada ACTUALIZA su fila al terminar; no se acumula historia. La lee la tarea
-- "TABLERO de Martin" de las 6:27 con una sola consulta, o `python3 -m herramientas.tablero`.
-- Proyecto Supabase: mop-estimador (sfmhdtingccfkzkwbqgt).

create table if not exists public.tablero (
  frente          text        not null check (length(frente) between 1 and 40),
  clave           text        not null check (length(clave) between 1 and 80),
  valor           text        not null check (length(valor) <= 300),
  fecha           timestamptz not null default now(),
  fuente          text        not null default '' check (length(fuente) <= 200),
  quien_escribio  text        not null check (length(quien_escribio) between 1 and 80),
  primary key (frente, clave)
);

comment on table public.tablero is
  'Números y estados del sistema de asistentes de MOP: una fila por (frente, clave), se pisa en cada corrida. Sin políticas: solo la escriben las tareas con Supabase (rol de servicio).';

-- Si una tarea reescribe su fila, la fecha se renueva sola.
create or replace function public.tablero_fecha()
returns trigger
language plpgsql
set search_path = ''
as $$
begin
  new.fecha := now();
  return new;
end;
$$;

create trigger tablero_fecha
  before insert or update on public.tablero
  for each row execute function public.tablero_fecha();

-- Repositorio público y clave publicable a la vista: RLS activo y SIN políticas, así que
-- con la clave publicable nadie lee ni escribe; solo el rol de servicio y execute_sql.
alter table public.tablero enable row level security;
