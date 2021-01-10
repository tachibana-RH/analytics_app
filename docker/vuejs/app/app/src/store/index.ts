import Vue from 'vue';
import Vuex, { StoreOptions } from 'vuex';
import { RootState } from './types';
import { ClientModule } from '@/store/menu/top';
import { ChildClientModule } from '@/store/menu/create_new_client';

Vue.use(Vuex);

const store: StoreOptions<RootState> = {
  state: {
    version: '1.0.0',
  },
  modules: {
    ClientModule,
    ChildClientModule
  },
};

export default new Vuex.Store<RootState>(store);