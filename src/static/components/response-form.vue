<template>
    <form action="#" class="response-form">
        <table>
            <tr>
                <td class="padded">Status Code</td>
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
                <td class="actions"></td>
            </tr>

            <tr v-for="header in headers">
                <td><input type="text" v-model="header.name"></td>
                <td><input type="text" v-model="header.value"></td>
                <td class="actions">
                    <button class="remove-btn" type="button">&times;</button>
                </td>
            </tr>

            <tr>
                <td colspan="3" class="padded">Response Body</td>
            </tr>
            <tr>
                <td colspan="3">
                    <textarea v-model="responseBody"></textarea>
                </td>
            </tr>

            <tr>
                <td colspan="3" class="form-actions">
                    <button class="send-btn">Send Response</button>
                    <button type="button" @click="addHeader">Add Header</button>
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
                statusCode: null,
                headers: [
                    { name: 'Content-Type', value: null }
                ],
                responseBody: null
            };
        },

        methods: {
            statusCodeGroup(min, max) {
                return this.statusCodeChoices
                    .filter(choice => choice.code >= min && choice.code <= max);
            },

            addHeader() {
                this.headers = [...this.headers, { name: null, value: null }];
            }
        }
    };
</script>

<style scoped>
    .response-form {
        padding: 0.4rem 0.8rem;
    }

    table {
        width: 100%;
        border-collapse: collapse;
        table-layout: fixed;
    }

    td {
        padding: 1px 0;
    }

    td:not(:first-child) {
        padding-left: 1px;
    }

    td:not(:last-child) {
        padding-right: 1px;
    }

    td.padded {
        padding: 0.4rem 0.5rem;
    }

    td.actions {
        width: 2.3rem;
    }

    td.form-actions {
        display: flex;
        padding-top: 0.4rem;
    }

    input,
    select,
    textarea {
        box-sizing: border-box;
        width: 100%;
        padding: 0.2rem 0.4rem;
        border: 1px solid var(--gray-1);
        border-radius: 2px;
        background-color: #fff;
    }

    select {
        -webkit-appearance: none;
    }

    textarea {
        display: block;
        resize: none;
    }

    button {
        padding: 0.2rem 0.4rem;
        border: 1px solid var(--gray-1);
        border-radius: 2px;
        text-transform: uppercase;
        background-color: #fff;
        cursor: pointer;
    }

    .remove-btn {
        width: 2.2rem;
        border: 1px solid var(--gray-1);
        background-color: #fff;
    }

    .send-btn {
        border: 1px solid var(--primary-color-dark-1);
        color: #fff;
        background-color: var(--primary-color);
    }

    .form-actions button:not(:last-child) {
        margin-right: 0.4rem;
    }
</style>
