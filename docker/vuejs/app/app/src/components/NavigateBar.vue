<template>
  <div id="nav">
    <p class="signout" @click="onSignOutClicked">sign out</p>
  </div>
</template>

<style lang="scss">
#nav {
  padding: 1rem;

  .signout {
    padding: 0.5rem;
    cursor: pointer;
  }
}
</style>>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { AxiosInstance, AxiosResponse, Method } from 'axios'
import { ApiRqsV1 } from '../methods/ApiRequestV1'


@Component
export default class NavigateBar extends Vue {

  public created(): void {

  }

  public async onSignOutClicked(): Promise<void> {
    const result = await ApiRqsV1('DELETE', '/auth/signout', {}, false).catch(err=>{console.log(err);});
    const result2 = await ApiRqsV1('DELETE', '/auth/signout_refresh', {}, true).catch(err=>{console.log(err);});
    this.$router.push('/');
  }
}
</script>