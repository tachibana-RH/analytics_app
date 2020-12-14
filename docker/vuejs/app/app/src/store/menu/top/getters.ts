import { GetterTree } from 'vuex';
import { RootState } from '@/store/types'
import { ClientState } from './types';

const getters: GetterTree<ClientState, RootState> = {
  size: (state: ClientState) => {
    return state.clients.length;
  },
  data: (state: ClientState) => {
    return state.clients;
  }
};

export default getters;