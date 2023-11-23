import Plotly from 'plotly.js-dist-min'

export default defineNuxtPlugin(() => {
  return{
    provide: {
      'Plotly': Plotly
    }
  }
})