<template>
  <div class="menu">
    <NavigateBar></NavigateBar>
    <List :items="analysLogs"></List>
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
import { ApiRqsV1 } from '../methods/ApiRequestV1';

// import { mapGetters ,mapActions } from 'vuex'

import NavigateBar from '@/components/NavigateBar.vue';
import List from '@/components/List.vue';

import { Refresh } from './types';


interface EstimateLog {
  id: number
  logs: object
}

@Component({
  // computed: {
  //   ...mapGetters('analys', {
  //     analysLogs: 'data'
  //   }),
  //   ...mapActions('analy', {
  //     analysSet: 'set',
  //     analysAdd: 'add',
  //     analysRemove: 'Remove',
  //   }),
  // },
  components: {
    NavigateBar,
    List,
  },
})
export class Estimate extends Vue {
  public analysLogs!: EstimateLog[];
  public analysSet!: any;

  public async beforeCreate(): Promise<void> {
    const res1: any = 
      await ApiRqsV1('POST', '/auth/refresh', {}, true)
      .catch(err=>{this.$router.push('/');});

    const res2: any = 
      await ApiRqsV1('GET', '/analytics/estimate', {}, false)
      .catch(err=>{this.$router.push('/');});

    //  this.analysLogs = res2['data'];
    //  this.analysSet(res2['data']);
    console.debug(res2['data']);
  }  
}
</script>