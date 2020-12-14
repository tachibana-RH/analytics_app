import { MutationTree } from 'vuex';
import { ClientChild, ClientChildState } from './types'

const mutations: MutationTree<ClientChildState> = {
  set: (state, data: ClientChild[]) => {
    state.clientchilds = data;
  },
  add: (state, data: ClientChild) => {
    state.clientchilds.push(data);
    state.clientchilds = state.clientchilds.map((v, i) => {
      v.f_child_index = i + 1;
      return v;
    });
  },
  remove: (state, idx: number) => {
    state.clientchilds = state.clientchilds.filter((e: ClientChild) => e.f_child_index !== idx);
    state.clientchilds = state.clientchilds.map((v, i) => {
      v.f_child_index = i + 1;
      return v;
    });
  },
};

export default mutations;