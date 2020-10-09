<template>
  <div class="menu">
    <NavigateBar></NavigateBar>
    welcome {{name}}!
    <router-link to="/analytics">Let's Analytics</router-link>
  </div>
</template>>

<style lang="scss">
.menu {
  text-align: center;
}
</style>>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { AxiosResponse } from 'axios';
import { ApiRqsV1 } from '../methods/ApiRequestV1'

import NavigateBar from '@/components/NavigateBar.vue';


@Component({
  components: {
    NavigateBar,
  },
})
export default class Menu extends Vue {
  public name: string = '';
  
  public async beforeCreate(): Promise<void> {
    const res1: any = await ApiRqsV1('POST', '/auth/refresh', {}, true).catch(err=>{this.$router.push('/');});
    const res2: any = await ApiRqsV1('GET', '/menu', {}, false).catch(err=>{this.$router.push('/');});
    this.name = res2['data']['name'];
  }
}
</script>