<template>
    <div class="container">
        <form>
            <div class="row">
                <div class="col-xs-12 col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3" v-if="!submittedData">
                    <!-- Exercise 1 -->
                    <!-- Create a Signup Form where you retrieve the following Information -->
                    <!-- Full Name (First Name + Last Name) -->
                    <!-- Mail -->
                    <!-- Password -->
                    <!-- Store Data? Yes/No -->
                    <app-full-name v-model="userData.fullName"></app-full-name>
                    
                    
                    <div class="form-group">
                        <label for="email"> Email </label>
                        <input id="email" class="form-control" type="email" v-model="userData.email">
                    </div>
                    <div class="form-group">
                        <label for="password"> Password </label>
                        <input id="password" class="form-control" type="password" v-model="userData.password">
                    </div>
                    <p> Store Data? </p>
                    <div class="form-group">
                        <label>
                            <input type="radio" value="Yes" v-model="storeData">Yes
                        </label>
                        <label>
                            <input type="radio" value="No" v-model="storeData">No
                        </label>
                    </div>
                    <button type="submit" @click.prevent="formSubmitted">Submit</button>


                    <!-- Exercise 2 -->
                    <!-- Only display the Form if it has NOT been submitted -->
                    <!-- Display the Data Summary ONCE the Form HAS been submitted -->

                    <!-- Exercise 3 -->
                    <!-- Edit the Example from above and create a custom "Full Name" Control -->
                    <!-- which still holds the First Name and Last Name Input Field -->
                </div>
            </div>
        </form>
        <hr>
        <div class="row">
            <div class="col-xs-12 col-sm-8 col-sm-offset-2 col-md-6 col-md-offset-3">
                <div class="panel panel-default">
                    <div class="panel-heading">
                        <h4>Your Data</h4>
                    </div>
                    <div class="panel-body" v-if="submittedData">
                        <p>Full Name: {{ userData.fullName }} </p>
                        <p>Mail: {{ userData.email }} </p>
                        <p>Password:  {{userData.password }}</p>
                        <p>Store in Database?: {{ storeData }} </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import FullName from "./components/fullName.vue"
    export default {
        data() {
            return {
                userData: {
                    fullName: '',
                    email: '',
                    password: '',
                    fullName: '',
                },
                submittedData: false,
                storeData: 'Yes',
            }
        },
        methods: {
            formSubmitted() {
                this.submittedData = true
            },

        },
        computed: {
            // makeFull() {
            //     this.userData.fullName = this.userData.firstName + ' ' + this.userData.lastName
            // }
        },
        components: {
            appFullName: FullName
        }
    }
</script>

<style>
</style>
