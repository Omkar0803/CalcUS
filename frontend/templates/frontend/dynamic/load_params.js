if ("{{ params.software }}" != "Unknown" && "{{ params.software }}" != "Open Babel") {
	solvent = document.getElementById("calc_solvent");
	solvent.value = "{{ params.solvent }}";

	solvation_model = document.getElementById("calc_solvation_model");
	solvation_model.value = "{{ params.solvation_model }}";

	solvation_radii = document.getElementById("calc_solvation_radii");
	solvation_radii.value = "{{ params.solvation_radii }}";

	software = document.getElementById("calc_software");
	software.value = "{{ params.software }}";

	theory_level = document.getElementById("calc_theory_level");
	theory_level.value = "{{ params.theory_level }}";

	basis_set = document.getElementById("calc_basis_set");
	basis_set.value = "{{ params.basis_set }}";

	{% if params.method == "PBEh-3c" %}
		pbeh3c = document.getElementById("pbeh3c");
		pbeh3c.checked = true;
	{% elif params.method == "HF-3c" %}
		hf3c = document.getElementById("hf3c");
		hf3c.checked = true;
	{% else %}
		func = document.getElementById("calc_functional");
		func.value = "{{ params.method }}";
	{% endif %}
	
	{% if load_charge %}
		charge = document.getElementById("calc_charge");
		charge.value = "{{ params.charge }}";
		mult = document.getElementById("calc_multiplicity");
		mult.value = "{{ params.multiplicity }}";
	{% endif %}

	df = document.getElementById("calc_df");
	df.value = "{{ params.density_fitting }}";

	bs = document.getElementById("calc_custom_bs");
	bs.value = "{{ params.custom_basis_sets }}";

    if("{{ params.software }}" != "xtb") {
        specifications = document.getElementById("calc_specifications");
        specifications.value = "{{ params.specifications }}";
    }
}
