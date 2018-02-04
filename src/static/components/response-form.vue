<template>
    <form action="#" class="response-form">
        <table>
            <tr>
                <td>Status Code</td>
                <td>
                    <select v-model="statusCode">
                        <optgroup label="Informational">
                            <option v-for="choice in statusCodeGroup(100, 199)" :value="choice.code">{{ choice.code }} {{ choice.text }}</option>
                        </optgroup>
                        <optgroup label="Success">
                            <option v-for="choice in statusCodeGroup(200, 299)" :value="choice.code">{{ choice.code }} {{ choice.text }}</option>
                        </optgroup>
                        <optgroup label="Redirection">
                            <option v-for="choice in statusCodeGroup(300, 399)" :value="choice.code">{{ choice.code }} {{ choice.text }}</option>
                        </optgroup>
                        <optgroup label="Client Errors">
                            <option v-for="choice in statusCodeGroup(400, 499)" :value="choice.code">{{ choice.code }} {{ choice.text }}</option>
                        </optgroup>
                        <optgroup label="Server Errors">
                            <option v-for="choice in statusCodeGroup(500, 599)" :value="choice.code">{{ choice.code }} {{ choice.text }}</option>
                        </optgroup>
                    </select>
                </td>
            </tr>
        </table>
    </form>
</template>

<script>
    import HttpChoicesMixin from '../mixins/http-choices';

    export default {
        mixins: [HttpChoicesMixin],

        data() {
            return {
                statusCode: null
            };
        },

        methods: {
            statusCodeGroup(min, max) {
                return this.statusCodeChoices
                    .filter(choice => choice.code >= min && choice.code <= max);
            }
        }
    };
</script>

<style scoped>
    .response-form {
        padding: 0.4rem 0.8rem;
    }
</style>
