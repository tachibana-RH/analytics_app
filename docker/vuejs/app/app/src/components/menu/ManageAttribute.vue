<template>
    <div class="manage_type">
        <md-field class="types">
            <label for="manage_type">Manages</label>
            <md-select name="f_manage_type" id="manage_type" v-model="value.f_manage_type">
                <md-option value="selecter">Selecter</md-option>
                <md-option value="id">ID</md-option>
                <md-option value="classname">Class Name</md-option>
                <md-option value="name">Name</md-option>
            </md-select>
        </md-field>
        <TextInput class="attr" :name="'f_manage_type_attr'" :placeholder="'attribute'" :type="'text'" v-model="value.f_manage_type_attr"></TextInput>
    </div>
</template>

<style lang="scss">
    .manage_type {
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
export default class ManageAttribute extends Vue {
    @Prop()
    private value!: ClientChild;
}
</script>>