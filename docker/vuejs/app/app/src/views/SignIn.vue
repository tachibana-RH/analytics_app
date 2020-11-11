<template>
  <div class="signin">
    <!-- <div id="sign_nav">
      <router-link to="/signup">Sign Up</router-link>
    </div> -->
    <div class="contents">
      <TextInput placeholder="username" type="text" v-model="name"></TextInput>
      <TextInput placeholder="password" type="password" v-model="pass"></TextInput>
      <SubmitButton method="POST" path="/auth/signin" :data="{username: name, password: pass}" @click="onMyButtonClicked">
        sign in
      </SubmitButton>
    </div>
  </div>
</template>

<style lang="scss">
.signin {
  height: 80vh;
  display: flex;
  justify-content: center;
  align-items: center;
  .contents{
    text-align: center;
    width: 20rem;
  }
  // #sign_nav {
  //   padding: 1rem;
  //   a {
  //     padding: 0.5rem;
  //   }
  //   &.router-link-exact-active {
  //     color: #42b983;
  //   }
  // }
}
</style>>

<script lang="ts">
  import { Component, Vue } from 'vue-property-decorator';
  import TextInput from '@/components/common/TextInput.vue';
  import SubmitButton from '@/components/common/SubmitButton.vue';
  import { AxiosResponse } from 'axios';

  @Component({
    components: {
      TextInput,
      SubmitButton,
    },
  })
  export default class SignIn extends Vue {
    public name: string = '';
    public pass: string = '';

    public onMyButtonClicked(response: Promise<AxiosResponse>): void {
      response.then(res => {
        console.log(res);
        this.$router.push('menu');
      })
      .catch(err => {
        console.log(err);
      });
    }
  }
</script>