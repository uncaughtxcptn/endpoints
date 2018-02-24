<template>
    <form action="#" class="response-form" @submit.prevent="onSubmit">
        <table>
            <tr>
                <td class="padded">Status Code</td>
                <td>
                    <select v-model="form.statusCode">
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

            <tr v-for="(header, index) in form.headers">
                <td><input type="text" v-model="header.name"></td>
                <td><input type="text" v-model="header.value"></td>
                <td class="actions">
                    <base-button class="mini remove-btn" @click="removeHeader(index)">&times;</base-button>
                </td>
            </tr>

            <tr>
                <td colspan="3" class="padded">Response Body</td>
            </tr>
            <tr>
                <td colspan="3">
                    <textarea v-model="form.responseBody"></textarea>
                </td>
            </tr>
        </table>

        <div class="form-actions">
            <base-button class="mini primary" type="submit">Set Response</base-button>
            <base-button class="mini" @click="addHeader">Add Header</base-button>
        </div>
    </form>
</template>

<script>
    import { httpStatusCodes } from '../lib/http-choices';

    export default {
        data() {
            return {
                form: {
                    statusCode: null,
                    headers: [
                        { name: 'Content-Type', value: null }
                    ],
                    responseBody: null
                }
            };
        },

        methods: {
            statusCodeGroup(min, max) {
                return httpStatusCodes.filter(choice => choice.code >= min && choice.code <= max);
            },

            addHeader() {
                this.form.headers = [...this.form.headers, { name: null, value: null }];
            },

            removeHeader(index) {
                this.form.headers = this.form.headers.filter((header, i) => i !== index);
            },

            onSubmit() {
                this.$emit('submit', {
                    statusCode: this.form.statusCode,
                    responseBody: this.form.responseBody,
                    headers: this.form.headers.reduce((headers, header) => {
                        if (header.name && header.name.trim() && header.value && header.value.trim()) {
                            headers.push({ name: header.name, value: header.value });
                        }
                        return headers;
                    }, [])
                });
            }
        },

        components: {
            'base-button': require('./base-button.vue').default
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
        width: 2.2rem;
    }

    .form-actions {
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

    .base-button {
        font-size: 1.2rem;
    }

    .remove-btn {
        width: 2.2rem;
    }

    .form-actions .base-button:not(:last-child) {
        margin-right: 0.4rem;
    }
</style>
