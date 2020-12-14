import { GetterTree } from 'vuex';
import { RootState } from '@/store/types';
import { ClientChildState } from './types'

const getters: GetterTree<ClientChildState, RootState> = {
  size: (state: ClientChildState) => {
    return state.clientchilds.length;
  },
  data: (state: ClientChildState) => {
    return state.clientchilds;
  },
  last: (state: ClientChildState) => {
    return state.clientchilds.slice(-1)[0];
  }
};

export default getters;