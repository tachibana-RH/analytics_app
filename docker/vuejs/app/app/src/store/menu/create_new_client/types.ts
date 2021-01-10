export interface ChildClientState {
  f_client_name: string
  f_category: string
  f_client_origin: string
  childclients: ChildClient[]
}

export interface ChildClient {
  f_child_index: number;
  f_child_client_name: string;
  f_manage_type: string;
  f_manage_type_attr: string;
  f_input_type: string;
  f_input_type_attr: string;
}

