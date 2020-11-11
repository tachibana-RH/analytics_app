<template>
  <div>{{ count }}</div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

@Component
export default class Counter extends Vue {
  // @Prop() private counter: number
  // incriment (): void {
  //   this.counter++;
  // }
}
</script>