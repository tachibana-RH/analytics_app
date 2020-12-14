import { MutationTree } from 'vuex';
import { ClientState, Client } from './types';

const mutations: MutationTree<ClientState> = {
  set: (state, data: Client[]) => {
    state.clients = data;
  },
  remove: (state, id: string) => {
    state.clients = state.clients.filter((e: Client) => e.f_client_id !== id);
  },
};

export default mutations;