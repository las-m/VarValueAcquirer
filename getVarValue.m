%This function takes a variable name and asks the expRunner for its value.
%Pass your variable as a string.
%The python modules use GETCURRENT
%You need python 3.2 in the default directory and scipy, numpy
function value = getVarValue(variable)

PythonPath = strcat(pwd,'\getVariables.py');
varFilePath = strcat(pwd,'\vars.mat');
%Call Python (over another method in an external file)
%errorHappened is 0 if everything went okay
try
    %Get the .mat file containing the variables
    [~, errorHappened] = python(PythonPath, varFilePath);
catch
    wanrdlg('Fatal Error while calling python.m')
end
try
    %Load the variables to matlab workspace
    variables = load(varFilePath);
catch
    warndlg('Could not find or open the file containing the variables.')
end
try
    %Get the value of the variable requested
    value = variables.(variable);
catch
    warndlg('An error occured. Most likely the variable your enetred does not exist.')
end
try
    %Delete the file containing the variables
    delete(varFilePath);
catch
    warndlg('Could not delete file containing the variables.')
end
end