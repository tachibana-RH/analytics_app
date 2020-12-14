<template>
  <div class="list">
    <ul>
      <li v-for="item in items" :key="item.data">
        {{ item.data }}
      </li>
    </ul>
  </div>
</template>>

<style lang="scss">
.list {
  ul {
    text-align: center;
  }
}
</style>>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

@Component({
  
})
export default class List extends Vue {
  private items!: object;

}
</script>