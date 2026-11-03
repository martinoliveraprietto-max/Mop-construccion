export type Cartel = { texto: string; leido: string }

declare module 'claude-code' {
  interface PluginState {
    'cerebro-mop': { cartel: Shaped<Cartel> }
  }
}
