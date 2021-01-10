import { MutationTree } from 'vuex';
import { ChildClient, ChildClientState } from './types'

const mutations: MutationTree<ChildClientState> = {
  set: (state, data: ChildClient[]) => {
    state.childclients = data;
  },
  add: (state, data: ChildClient) => {
    state.childclients.push(data);
    state.childclients = state.childclients.map((v, i) => {
      v.f_child_index = i + 1;
      return v;
    });
  },
  remove: (state, idx: number) => {
    state.childclients = state.childclients.filter((e: ChildClient) => e.f_child_index !== idx);
    state.childclients = state.childclients.map((v, i) => {
      v.f_child_index = i + 1;
      return v;
    });
  },
};

export default mutations;