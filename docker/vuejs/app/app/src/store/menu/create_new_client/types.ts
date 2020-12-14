export interface ClientChildState {
  f_client_name: string
  f_category: string
  f_client_origin: string
  clientchilds: ClientChild[]
}

export interface ClientChild {
  f_child_index: number;
  f_child_client_name: string;
  f_manage_type: string;
  f_manage_type_attr: string;
  f_input_type: string;
  f_input_type_attr: string;
}

