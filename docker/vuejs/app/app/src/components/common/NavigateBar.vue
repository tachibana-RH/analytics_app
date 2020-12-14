<template>
  <div class="navi">
    <!-- <p class="signout" @click="onSignOutClicked">sign out</p> -->
    <md-menu md-direction="bottom-end">
      <md-button @click="onSignOutClicked">sign out</md-button>
      <md-button v-show="!isCreateDisplay" @click="onCreateClicked">create new client</md-button>
      <md-button v-show="isCreateDisplay" @click="onBackTopPage">back clients list</md-button>
    </md-menu>
    <md-menu md-size="big" md-direction="top-start" style="float: right;">
      <md-button class="md-icon-button" md-menu-trigger>
        <md-icon>account_box</md-icon>
      </md-button>
      <md-menu-content>
        <div class="author-card">
          <md-avatar class="md-large">
            <img src="../../assets/human.png" alt="user">
          </md-avatar>
          <!-- <div class="author-card-info">
            <span>{{ name }}</span>
            <div class="author-card-links">
              <a href="https://linkedin.com/in/marcosvmmoura" target="_blank" rel="noopener">Linkedin</a>
              <a href="https://github.com/marcosmoura" target="_blank" rel="noopener">GitHub</a>
            </div>
          </div> -->
          <span>{{ name }}</span>
        </div>
      </md-menu-content>
    </md-menu>
  </div>
</template>

<style lang="scss">
.navi {
  padding: 1rem;

  .signout {
    padding: 0.5rem;
    cursor: pointer;
  }
}
</style>>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
import { AxiosInstance, AxiosResponse, Method } from 'axios'
import { ApiRqsV1 } from '../../methods/ApiRequestV1'


@Component
export default class NavigateBar extends Vue {

  @Prop()
  private name!: string;
  @Prop()
  private isCreateDisplay!: boolean;

  public created(): void {

  }

  private async onSignOutClicked(): Promise<void> {
    const result = await ApiRqsV1('DELETE', '/auth/signout', {}, false).catch(err=>{console.log(err);});
    const result2 = await ApiRqsV1('DELETE', '/auth/signout_refresh', {}, true).catch(err=>{console.log(err);});
    this.$router.push('/');
  }

  private async onCreateClicked(): Promise<void> {
    this.$router.push('/create');
  }

  private onBackTopPage(): void {
    this.$router.push('/menu');
  }
}
</script>