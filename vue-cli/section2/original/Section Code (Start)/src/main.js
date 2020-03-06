import Vue from 'vue'
import App from './App.vue'

export const eventBus = new Vue({
  methods: {
    changeAge() {
      // this.$emit('ageWasEdited', age);
      // eventBus.$emit('ageWasEdited', this.userAge);
      eventBus.changedAge(this.userAge)
    }
  }
});

new Vue({
  el: '#app',
  render: h => h(App)
})

