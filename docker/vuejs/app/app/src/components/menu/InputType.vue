<template>
    <div class="input_type">
        <md-field class="types">
            <label for="input_type">Type</label>
            <md-select name="f_input_type" id="input_type" v-model="value.f_input_type">
                <md-option value="text">Text</md-option>
                <md-option value="select">Select</md-option>
                <md-option value="radio">Radio</md-option>
                <md-option value="submit">Submit</md-option>
                <md-option value="js">Script</md-option>
            </md-select>
        </md-field>
        <TextInput class="attr" :name="'f_input_type_attr'" :placeholder="'attribute'" :type="type" v-model="value.f_input_type_attr"></TextInput>
    </div>
</template>

<style lang="scss">
    .input_type {
        text-align: center;
        .types {
            display: inline-block;
            width: 20vw;
            margin: 1rem;
        }
        .attr {
            display: inline-block;
            width: 40vw;
            margin: 1rem;
        }
    }
</style>

<script lang="ts">
import { Component, Emit, Prop, Vue } from 'vue-property-decorator';
import TextInput from '@/components/common/TextInput.vue';
import { ClientChild } from '../../store/menu/create_new_client/types';

@Component({
    components: {
        TextInput
    }
})
export default class TextInputDynamic extends Vue {
    private type: string = "text";

    @Prop()
    value!: ClientChild;
}
</script>>