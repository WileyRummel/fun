<template>
    <div class="bar">
        <h3> Quotes Added </h3>
        <hr>
        <div class="boxwrap">
        <p> {{ quoteNum() }} /10 </p>
        </div>
    </div>
    
</template>

<script>
export default {
    data() {
        return {
            QuotesAdded: ["hello"],

        }
    },
    methods: {
        quoteNum() {
            return QuotesAdded.length
        }
    },    
}
</script>

<style scoped>

    .boxwrap {
        border: 1px solid darkgray;
        border-radius: 2%;
        background-color: lightgray;
    }
    p {
        border: 1px solid darkgray;
        border-radius: 2%;
        background-color: lightblue;
        width: 10%;

    }
</style>