<template>
    <div class="create-new-client">
        <NavigateBar :name="name" :isCreateDisplay="true"></NavigateBar>
        <div class="contents">
            <div class="wrap-parent">
                <TextInput class="parent client-name" placeholder="Client Name" v-model="clientChildState.f_client_name"></TextInput>
                <TextInput class="parent category" placeholder="Category Name" v-model="clientChildState.f_category"></TextInput>
                <TextInput class="origin" placeholder="Origin URL" v-model="clientChildState.f_client_origin"></TextInput>
            </div>
            <v-expansion-panels>
                <draggable class="panels" v-model="clientChildState.clientchilds" group="clientsGroup" @start="drag=true" @end="drag=true" :animation="200">
                    <v-expansion-panel
                    v-for="(clientChild, i) in clientChildState.clientchilds"
                    :key="i"
                    >
                    <div class="wrap-remove-client">
                        <a class="remove-client" @click="onRemoveInstruction(i)">
                            <md-icon>delete_forever</md-icon>
                        </a>
                    </div>
                    <v-expansion-panel-header>
                        <div><TextInput class="title" placeholder="Title" v-model="clientChildState.clientchilds[i].f_child_client_name"></TextInput></div>
                    </v-expansion-panel-header>
                    <v-expansion-panel-content>
                        <ManageAttribute v-model="clientChildState.clientchilds[i]"></ManageAttribute>
                        <InputType v-model="clientChildState.clientchilds[i]"></InputType>
                    </v-expansion-panel-content>
                    </v-expansion-panel>
                </draggable>
            </v-expansion-panels>
            <a class="add-client" @click="onAddInstruction">
                <md-icon>add_task</md-icon>
            </a>
        </div>
    </div>
</template>

<style lang="scss" scoped>
    .create-new-client {
        .contents {
            margin: auto;
            border-radius: 4px;
            width: 80vw;
            .parent {
                display: inline-block;
                width: 20vw;
                margin-right: 1rem;
            }
            .panels {
                width: 80vw;
            }
            .title {
                width: 30vw;
            }
            .add-client {
                cursor: pointer;
            }
            .wrap-remove-client {
                text-align: right;
                .remove-client {
                    cursor: pointer;
                }
            }
        }
    }
</style>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
import draggable from 'vuedraggable';
import NavigateBar from '@/components/common/NavigateBar.vue';
import InputType from '@/components/menu/InputType.vue';
import ManageAttribute from '@/components/menu/ManageAttribute.vue';
import TextInput from '@/components/common/TextInput.vue';

import { ApiRqsV1 } from '../../methods/ApiRequestV1';

import { State, Action, Getter } from 'vuex-class';
import { ClientChildState, ClientChild } from '../../store/menu/create_new_client/types';
const namespace: string = 'ClientChildModule';

@Component({
    components: {
        draggable,
        NavigateBar,
        InputType,
        ManageAttribute,
        TextInput
    }
})
export default class CreateNewClient extends Vue {

    @State('ClientChildModule') private clientChildState!: ClientChildState;
    @Action('set', { namespace }) private setClientChild: any;
    @Action('add', { namespace }) private addClientChild: any;
    @Action('remove', { namespace }) private remClientChild: any;
    @Getter('size', { namespace }) private sizeClientChild: any;
    @Getter('last', { namespace }) private lastClientChild: any;

    private name: string = '';
    private drag!: boolean;
    private initData: ClientChild[] = [
        {
            f_child_index: 1,
            f_child_client_name: "",
            f_manage_type: "",
            f_manage_type_attr: "",
            f_input_type: "",
            f_input_type_attr: "",
        }
    ];
    
    public async beforeCreate(): Promise<void> {
        const res: any = await ApiRqsV1('GET', '/menus', {}, false)
                                .catch(err => {this.$router.push({name:'signin'});});
        this.name = res['data']['f_user_name'];

        this.setClientChild(this.initData);
    }

    private onAddInstruction(): void {
        let baseData: ClientChild = {
            f_child_index: 0,
            f_child_client_name: "",
            f_manage_type: "",
            f_manage_type_attr: "",
            f_input_type: "",
            f_input_type_attr: "",
        };
        baseData.f_child_index = this.sizeClientChild === 0 ?
                                    1 : this.lastClientChild.f_child_index + 1;
        this.addClientChild(baseData);
        console.log(this.clientChildState.clientchilds);
    }

    private onRemoveInstruction(i: number): void {
        this.sizeClientChild !== 1 ?
            this.remClientChild(i+1):
            console.log(this.clientChildState.clientchilds);
    }

}
</script>>