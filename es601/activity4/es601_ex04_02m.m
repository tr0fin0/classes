%%============================================================================
%%                    Main Code
%%============================================================================
clear all
close all

%%  Question 2A
%%============================================================================
%%    Equation
k = 0:10;
n = length(k);

for i=1:n
    y(i)=25/8*(0.2^k(i) - 1) + 5/2*k(i);
end
stairs(k,y);

%%    Recursion
yr(1) = 0;
for j=0:9
    yr(j+2) = 0.2*yr(j+1) + 2*j;
end
hold on
stairs(k,yr,'+');
hold off

%%  Question 2B
%%============================================================================
%%    Recursion
yr(1) = 5;
for j=0:9
    yr(j+2) = 5*0.2^(j+1);
end
stairs(k,yr);