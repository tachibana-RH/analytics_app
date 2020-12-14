import { Module } from 'vuex';
import { RootState } from '@/store/types'
import { ClientState } from './types';
import getters from './getters';
import actions from './actions';
import mutations from './mutations';

const state: ClientState = {
  clients: []
};

export const ClientModule: Module<ClientState, RootState> = {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};