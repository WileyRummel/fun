<template>
  <div id="app">
    <img src="./assets/logo.png">
    <h1>{{ msg }}</h1>
    <app-servers></app-servers>
    <hr>
    <bottom-details></bottom-details>
  </div>
</template>

<script>
export default {
  name: 'app',
  data: function() {
    return {
      msg: 'HELLO WORLD'
    }
  }
}
</script>

