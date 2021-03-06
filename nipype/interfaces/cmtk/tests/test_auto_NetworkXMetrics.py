# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..nx import NetworkXMetrics


def test_NetworkXMetrics_inputs():
    input_map = dict(
        compute_clique_related_measures=dict(usedefault=True, ),
        in_file=dict(
            extensions=None,
            mandatory=True,
        ),
        out_edge_metrics_matlab=dict(
            extensions=None,
            genfile=True,
        ),
        out_global_metrics_matlab=dict(
            extensions=None,
            genfile=True,
        ),
        out_k_core=dict(
            extensions=None,
            usedefault=True,
        ),
        out_k_crust=dict(
            extensions=None,
            usedefault=True,
        ),
        out_k_shell=dict(
            extensions=None,
            usedefault=True,
        ),
        out_node_metrics_matlab=dict(
            extensions=None,
            genfile=True,
        ),
        out_pickled_extra_measures=dict(
            extensions=None,
            usedefault=True,
        ),
        treat_as_weighted_graph=dict(usedefault=True, ),
    )
    inputs = NetworkXMetrics.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_NetworkXMetrics_outputs():
    output_map = dict(
        edge_measure_networks=dict(),
        edge_measures_matlab=dict(extensions=None, ),
        global_measures_matlab=dict(extensions=None, ),
        gpickled_network_files=dict(),
        k_core=dict(extensions=None, ),
        k_crust=dict(extensions=None, ),
        k_networks=dict(),
        k_shell=dict(extensions=None, ),
        matlab_dict_measures=dict(),
        matlab_matrix_files=dict(),
        node_measure_networks=dict(),
        node_measures_matlab=dict(extensions=None, ),
        pickled_extra_measures=dict(extensions=None, ),
    )
    outputs = NetworkXMetrics.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
