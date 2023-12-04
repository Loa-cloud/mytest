
#include <gtest/gtest.h>
#include <gmock/gmock-matchers.h>

extern "C" {
#include "myfunc.h"
}

using namespace testing;

TEST(root_test, positive_d)
{
    double a, b, c, x1, x2;
    double x1_answ, x2_answ;
    x1_answ = 2;
    x2_answ = 1;

    a = 1;
    b = -3;
    c = 2;
    root(a, b, c, &x1, &x2);

    ASSERT_EQ(x1, x1_answ);
    ASSERT_EQ(x2, x2_answ);
}

TEST(root_test, zero_d)
{
    double a, b, c, x1, x2;
    double x1_answ, x2_answ;
    x1_answ = 0.25;
    x2_answ = 0.25;

    a = 16;
    b = -8;
    c = 1;
    root(a, b, c, &x1, &x2);

    ASSERT_EQ(x1, x1_answ);
    ASSERT_EQ(x2, x2_answ);
}

TEST(root_test, negative_d)
{
    double a, b, c, x1, x2;
    double x1_answ, x2_answ;
    x1_answ = -999;
    x2_answ = -999;

    x1 = -999;
    x2 = -999;
    a = 3;
    b = 1;
    c = 2;
    root(a, b, c, &x1, &x2);

    ASSERT_EQ(x1, x1_answ);
    ASSERT_EQ(x2, x2_answ);
}


TEST(root_test, zero_c1)
{
    double a, b, c, x1, x2;
    double x1_answ, x2_answ;
    x1_answ = 0;
    x2_answ = 5.2;

    a = 5;
    b = -26;
    c = 0;
    root(a, b, c, &x1, &x2);

    ASSERT_EQ(x1, x1_answ);
    ASSERT_EQ(x2, x2_answ);
}

TEST(root_test, zero_c2)
{
    double a, b, c, x1, x2;
    double x1_answ, x2_answ;
    x1_answ = 0;
    x2_answ = -16;

    a = 4;
    b = 64;
    c = 0;
    root(a, b, c, &x1, &x2);

    ASSERT_EQ(x1, x1_answ);
    ASSERT_EQ(x2, x2_answ);
}

TEST(root_test, zero_b1)
{
    double a, b, c, x1, x2;
    double x1_answ, x2_answ;
    x1_answ = -7;
    x2_answ = 7;

    a = 1;
    b = 0;
    c = -49;
    root(a, b, c, &x1, &x2);

    ASSERT_EQ(x1, x1_answ);
    ASSERT_EQ(x2, x2_answ);
}

TEST(root_test, zero_b2)
{
    double a, b, c, x1, x2;
    double x1_answ, x2_answ;
    x1_answ = -999;
    x2_answ = -999;

    x1 = -999;
    x2 = -999;

    a = 1;
    b = 0;
    c = 3;
    root(a, b, c, &x1, &x2);

    ASSERT_EQ(x1, x1_answ);
    ASSERT_EQ(x2, x2_answ);
}

TEST(root_test, zero_b_c)
{
    double a, b, c, x1, x2;
    double x1_answ, x2_answ;
    x1_answ = 0;
    x2_answ = 0;

    a = 5;
    b = 0;
    c = 0;
    root(a, b, c, &x1, &x2);

    ASSERT_EQ(x1, x1_answ);
    ASSERT_EQ(x2, x2_answ);
}

TEST(root_test, zero_a)
{
    double a, b, c, x1, x2;
    double x1_answ, x2_answ;
    x1_answ = -999;
    x2_answ = -999;

    x1 = -999;
    x2 = -999;

    a = 0;
    b = 9;
    c = 78;
    root(a, b, c, &x1, &x2);

    ASSERT_EQ(x1, x1_answ);
    ASSERT_EQ(x2, x2_answ);
}

