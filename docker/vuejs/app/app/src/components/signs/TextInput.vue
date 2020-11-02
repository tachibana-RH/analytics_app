<template>
  <input type="text" :placeholder="placeholder" v-model="textValue">
</template>

<script lang="ts">
  import {Component, Emit, Prop, Vue} from 'vue-property-decorator';

  @Component
  export default class TextInput extends Vue {

    @Prop()
    public placeholder?: string;

    /** モデルバインドのために記述必須 */
    @Prop()
    public value!: string;

    /** モデルバインドのために記述必須 */
    @Emit()
    public input(value: string) {
      // no work
    }

    private get textValue(): string {
      return this.value;
    }

    private set textValue(val: string) {
      this.input(val);
    }
  }
</script>>