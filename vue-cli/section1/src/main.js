import Vue from 'vue'
import App from './App.vue'
import Home from './components/Home.vue'
import Footer from './components/Footer.vue'

Vue.component('bottom-details', Footer)
Vue.component('app-servers', Home)
new Vue({
  el: '#app',
  render: h => h(App)
})
