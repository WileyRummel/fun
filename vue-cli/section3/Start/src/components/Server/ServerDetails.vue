<template>
    <div class="col-xs-12 col-sm-6">
        <p v-if="!server"> Select a server </p>
        <p v-else> 
           Server #{{ server.id }} selected, Server Status: {{ server.status }}
        </p>
        <button @click="statusReset"> Change Status to Normal </button>
    </div>

</template>

<script>
    import { serverBus}  from "../../main";

    export default {
        data () {
                return {  
                    server: null
                }
            },
        methods: {
            statusReset() {
                this.server.status = "Normal"
            }
        },
        created() {
            serverBus.$on("serverSelected", (server) =>  {
                this.server = server;}
            )
        }
    }
</script>

<style>

</style>
