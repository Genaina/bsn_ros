#ifndef CONTROLLER_NODE_HPP
#define CONTROLLER_NODE_HPP

#include <sstream>
#include <string>
#include <fstream>
#include <map>

#include "ros/ros.h"

#include "goalmodel/Node.hpp"
#include "goalmodel/Goal.hpp"
#include "goalmodel/Task.hpp"
#include "goalmodel/Property.hpp"
#include "goalmodel/LeafTask.hpp"
#include "goalmodel/Context.hpp"
#include "goalmodel/GoalTree.hpp"

#include "lepton/Lepton.h"

#include "FormulaRefs.hpp"
#include "model/Formula.hpp"


#include "bsn/TaskInfo.h"
#include "bsn/ControlCommand.h"
#include "bsn/ControlCentralhub.h"
#include "bsn/ContextInfo.h"

class ControllerNode {

    private:
      	ControllerNode(const ControllerNode &);
    	ControllerNode &operator=(const ControllerNode &);

  	public:
      	void setUp();

		void setTaskValue(std::string, double);
		double getTaskValue(std::string);

		bool isCost(std::string);

    	ControllerNode(int &argc, char **argv, std::string name);
    	virtual ~ControllerNode();

		void receiveTaskInfo(const bsn::TaskInfo::ConstPtr& /*msg*/);
		void receiveContextInfo(const bsn::ContextInfo::ConstPtr& /*msg*/);

    	void analyze(std::string);
    	void plan(std::string, double, double);
    	void execute(std::string, double, double, double);

		void run();

  	private:

	std::map<std::string, double> tasks;
	std::map<std::string, bsn::goalmodel::Context> contexts;

	// May be redundant... should try to refactor it later
	std::vector<std::string> props;
	std::vector<double> values;

	double reli_value;
	double cost_value;
	double reli_error;
	double cost_error;

	bsn::model::Formula cost_expression;
	bsn::model::Formula reliability_expression;
/* 
	std::map<std::string,double&> cost_formula_reliabilities;
	std::map<std::string,double&> cost_formula_frequencies;
	std::map<std::string,double&> cost_formula_costs;
	std::map<std::string,double&> cost_formula_contexts;

	std::map<std::string,double&> reliability_formula_reliabilities;
	std::map<std::string,double&> reliability_formula_frequencies;
	std::map<std::string,double&> reliability_formula_contexts;

	std::vector<std::vector<double>> actions;

	double cost_setpoint;
	double reliability_setpoint;
 */
};

#endif 