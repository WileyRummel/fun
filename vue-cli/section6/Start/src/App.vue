<template>
    <div class="container">
        <app-progress-bar :quoteCount="quotes.length" :maxQuotes="maxQuotes"></app-progress-bar>
        <app-new-quote @quoteAdded="newQuote"> </app-new-quote>
        
        <app-quote-grid :quotes="quotes" @quoteDeleted="deleteQuote"></app-quote-grid>

        <div class="row">
            <div class="col-sm-12 text-center">
                <div class="alert alert-info">Info: Click on a quote to delete it</div>

            </div>
        </div>
    
    </div>
</template>

<script>
import QuoteGrid from'./components/QuoteGrid.vue';
import NewQuote from './components/NewQuote.vue';
import progressbar from './components/progressbar.vue';
    export default {
    data: function() {
         return {
             maxQuotes: 10,
             quotes: [
                 'Just a test Quote',
             ],
         }
     },
    methods: {
            newQuote(quote) {
                if (this.quotes.length >= this.maxQuotes) { 
                    return alert("Please delete a quote first. Only 10 quotes allowed")
                }
                this.quotes.push(quote)
            },
            deleteQuote(index) {
                this.quotes.splice(index, 1);
            },
     },
    components: {
        appQuoteGrid: QuoteGrid,
        appNewQuote: NewQuote,
        appProgressBar: progressbar,

     }   
    }
</script>

<style>
</style>
