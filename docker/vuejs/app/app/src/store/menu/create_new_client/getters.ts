import { GetterTree } from 'vuex';
import { RootState } from '@/store/types';
import { ChildClientState } from './types'

const getters: GetterTree<ChildClientState, RootState> = {
  size: (state: ChildClientState) => {
    return state.childclients.length;
  },
  data: (state: ChildClientState) => {
    return state.childclients;
  },
  last: (state: ChildClientState) => {
    return state.childclients.slice(-1)[0];
  }
};

export default getters;