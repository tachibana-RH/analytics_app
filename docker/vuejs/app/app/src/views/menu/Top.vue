<template>
  <div class="menu">
    <NavigateBar :name="name" :isCreateDisplay="false"></NavigateBar>
    <div class="contents">
      <md-empty-state v-if="clients.length === 0"
        md-label="Create your first project"
        md-description="Creating project, you'll be able to upload your design and collaborate with people.">
        <md-button class="md-primary md-raised" @click="onCreate">Create first client</md-button>
      </md-empty-state>
    </div>
  </div>
</template>>

<style lang="scss">
.menu {
  .contents {
    text-align: center;
  }
}
</style>>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { AxiosResponse } from 'axios';
import { ApiRqsV1 } from '../../methods/ApiRequestV1'

import NavigateBar from '@/components/common/NavigateBar.vue';


@Component({
  components: {
    NavigateBar,
  },
})
export default class Menu extends Vue {
    private name: string = '';
    private clients: object = [];
  
    public async beforeCreate(): Promise<void> {
        const res: any = await ApiRqsV1('GET', '/menus', {}, false)
            .catch(err => {this.$router.push({name:'signin'});});
        this.name = res['data']['f_user_name'];
        this.clients = res['data']['clients'];
    }

    private onCreate() {
        this.$router.push({name: 'menu.create'});
    }
}
</script>