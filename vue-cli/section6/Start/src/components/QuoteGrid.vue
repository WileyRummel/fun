<template>
    <div class="row">
        <app-quote v-for="(quote, index) in quotes" v-bind:key="(quote, index)" @click.native="deleteQuote">
            {{ quote }}
        </app-quote>
    
    </div>
</template>
<script>
import Quote from './Quote.vue'
export default {
    props: ['quotes'],
    components: {
        appQuote: Quote
    },
    methods: {
        deleteQuote(index) {
            this.$emit('quoteDeleted', index)
        }
    }

}
</script>

<style scoped>

</style>