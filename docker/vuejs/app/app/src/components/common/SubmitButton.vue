<template>
  <md-button @click="onClick">
    <slot></slot>
  </md-button>
</template>

<script lang="ts">
  import { Component, Emit, Prop, Vue } from 'vue-property-decorator';
  import { AxiosResponse, Method } from 'axios'
  import { ApiRqsV1 } from '../../methods/ApiRequestV1'


  @Component
  export default class SubmitButton extends Vue {
    @Prop()
    private method!: Method;
    @Prop()
    private path!: string;
    @Prop()
    private data?: object;

    private response!: Promise<AxiosResponse>;

    @Emit()
    public click(res: Promise<AxiosResponse>) {
      // no work
    }

    public created(): void {
     // no work 
    }

    public onClick(): void {
      this.response = ApiRqsV1(this.method, this.path, this.data, false);
      this.click(this.response);
    }
  }
</script>