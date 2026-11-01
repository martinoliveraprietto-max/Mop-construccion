import { atom, read, update } from 'claude-code'
import type { EngineInterface, Register } from 'claude-code'

import type { Cartel } from '../types'

// Panel de Cerebro MOP (pedido de Martin, 1-nov-2026): muestra CALIENTE.md, el cartel con
// lo urgente de hoy, al lado del chat. Se actualiza al abrir la sesión, con /cerebro y con
// el botón "Actualizar".
const PANEL = 'cerebro-mop'
const cartel = atom({ plugin: 'cerebro-mop', key: 'cartel' } as const,
  { texto: '', leido: '' }, { shape: 'cartel-1' })

async function leerCartel($: EngineInterface) {
  let texto = 'No encontré CALIENTE.md en la carpeta del proyecto.'
  try {
    const raiz = await $.session.root()
    texto = await $.fs.read(`${raiz}/CALIENTE.md`)
  } catch {}
  const ahora = new Date().toLocaleTimeString('es-UY', { hour: '2-digit', minute: '2-digit' })
  await update($, cartel, (): Cartel => ({ texto, leido: ahora }))
}

export const register: Register = on => {
  on('session.start', async ($, e, next) => {
    await $.command.register({ name: 'cerebro', description: 'Abre el panel Cerebro MOP con lo urgente de hoy' })
    await leerCartel($)
    void $.ui.open({ id: PANEL, title: 'Cerebro MOP' })
    return next(e)
  })

  on('command.run', { command: 'cerebro' }, async $ => {
    await leerCartel($)
    await $.ui.open({ id: PANEL, title: 'Cerebro MOP' })
    return { text: 'Panel Cerebro MOP abierto.' }
  })

  on('ui.render', { component: 'Pane', requestId: PANEL }, async ($, e) => {
    const { Box, Text, Button } = $.ui.resolve(e)
    const { texto, leido } = await read($, cartel)
    const lineas = texto.split('\n').filter(l => l.trim() !== '')
    return (
      <Box flexDirection="column">
        <Button onPress={() => leerCartel($)}>Actualizar</Button>
        {leido !== '' && <Text dimColor>Leído a las {leido}</Text>}
        {lineas.map(l =>
          l.startsWith('#')
            ? <Text bold>{l.replace(/^#+\s*/, '')}</Text>
            : <Text>{l}</Text>)}
      </Box>
    )
  })
}
