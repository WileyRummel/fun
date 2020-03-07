<template>
  <div>
    <h3>New Quote</h3>
    <button @click="counter++">Increase countS</button>
    <p> {{ counter }}</p>
  </div>
</template>

<script>
export default {
    data() {
        return {
            counter: 0
        };
    },
    destroyed() {
        console.log("DESTROYED")
    },
    deactivated() {
        console.log("DEACTIVATED")
    },
    activated() {
        console.log("ACTIVATED")
    }
}
</script>