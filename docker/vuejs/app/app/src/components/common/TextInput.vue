<template>
  <md-field>
    <label>{{ placeholder }}</label>
    <md-input :name="name" :type="type" v-model="textValue"></md-input>
  </md-field>
</template>

<script lang="ts">
  import {Component, Emit, Prop, Vue} from 'vue-property-decorator';

  @Component
  export default class TextInput extends Vue {
    @Prop()
    private name?: string;
    @Prop()
    private type?: string;
    @Prop()
    private placeholder?: string;

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