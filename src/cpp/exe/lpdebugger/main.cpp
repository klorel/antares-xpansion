
#include <iostream>
#include <fstream>
#include <sstream>
#include <boost/program_options.hpp>

#include "SolverFactory.h"
#include "ortools_utils.h"

namespace po = boost::program_options;

int main(int argc, char** argv){
	if (argc <= 1) {
		std::cout << "usage: lp_debugger.exe <path_to_mps_file> " << std::endl;
		return 0;
	}
	std::string const mps_path(argv[1]);
	std::cout << "mps_path is : " << mps_path << std::endl;
	SolverFactory f;
	auto solver = f.create_solver("CLP");
	solver->init();
	solver->set_output_log_level(3);
	solver->read_prob(mps_path.c_str(), "");
	int lp_status(-1);
	solver->solve_lp(lp_status);
	std::cout << "lp_status : " << lp_status << std::endl;
	return 0;
}