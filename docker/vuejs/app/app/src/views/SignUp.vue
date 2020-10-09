<template>
  <div class="signup">
    <div id="sign_nav">
      <router-link to="/">Sign In</router-link>
    </div>
    <TextInput placeholder="username" v-model="name"></TextInput>
    <TextInput placeholder="password" v-model="pass"></TextInput>
    <SubmitButton method="POST" path="/auth/signup" :data="{'username': name, 'password': pass}" @click="onMyButtonClicked">
      let's sign up
    </SubmitButton>
  </div>
</template>

<style lang="scss">
.signup {
  text-align: center;

  #sign_nav {
    padding: 1rem;
    a {
      padding: 0.5rem;
    }
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>>

<script lang="ts">
  import { Component, Vue } from 'vue-property-decorator';
  import TextInput from '@/components/TextInput.vue';
  import SubmitButton from '@/components/SubmitButton.vue';
  import { AxiosResponse } from 'axios';

  @Component({
    components: {
      TextInput,
      SubmitButton,
    },
  })
  export default class SignUp extends Vue {
    public name: string = '';
    public pass: string = '';

    public onMyButtonClicked(response: Promise<AxiosResponse>): void {
      response.then(res => {
        console.log(res);
        alert('Success! Please Sign In!');
      })
      .catch(err => {
        console.log(err);
        alert('Failed...');
      });
    }
  }
</script>