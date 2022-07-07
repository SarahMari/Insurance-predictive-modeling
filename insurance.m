
function prediction = insurance(file_name)

data = csvread(file_name);
[a ,b] = size(data);
%split into X and Y
X = data(:,1:(b-1));
y = data(:,b);

[m, n] = size(X);

% Add intercept term to X and X_test
X = [ones(m, 1) X];

%split into test and train

%randomize training set

train_size = round(m*.75);
test_size = m - train_size;
X_train = X(1: train_size,:);
y_train = y(1: train_size, :);

X_test = X(test_size:m, :);
y_test = y(test_size:m, :);

%SHOULD go back and randomize init_theta! ???
init_theta = ones(n+1, 1);
J = 0;
X_grad = zeros(size(X));
Theta_grad = zeros(size(init_theta));

%lambda
lambda = 10

[J, grad] = linearRegCostFunction(X_train, y_train, init_theta, lambda);
J


% Set Options
options = optimset('GradObj', 'on', 'MaxIter', 400);

% Optimize
%[theta, J, exit_flag] = ...
%	fminunc(@(t)(linearRegCostFunction(t, X_train, y_train,lambda)), init_theta, options);

[theta] = trainLinearReg([ones(m, 1) X], y, lambda);


predictions = X_test * theta(2:end, :);
predictions(1:10)
y_test(1:10)

%calculate RMSE/(max-min) close to zero is good
RMSE = sqrt(sum((predictions - y_test).^2)/test_size);

%calculate normalized RMSE
n_RMSE = RMSE/(max(y_test)-min(y_test));

comp = X_train *theta(2:end, :);
RMSE = sqrt(sum((comp - y_train).^2)/train_size)

%calculate normalized RMSE
n_RMSE = RMSE/(max(y_train)-min(y_train))

%Next steps ideas:
% Randomize init_theta
% Get RMSE for training set to see if high bias vs variance
% Do random values for training set instead of first 1000



endfunction
