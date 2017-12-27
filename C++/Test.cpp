#include "gtest/gtest.h"
#include "Employees.h"
#include "ScreenInfo.h"
#include <string>

TEST(TestCaseName, TestName) {
  EXPECT_EQ(1, 1);
  EXPECT_TRUE(true);
}

TEST(FulltimeTest, TypeIsFT)
{
     std::string name = "Jane Shepard";
     Fulltime shepard = Fulltime(name, 1.0);
     EXPECT_EQ(shepard.getType(), "[FT]");
}

TEST(ContractorTest, TypeIsC)
{
     std::string name = "Zaeed Massani";
     Contractor zaeed = Contractor(name, 1.0);
     EXPECT_EQ(zaeed.getType(), "[C]");
}

TEST(TemporaryTest, TypeIsT)
{
     std::string name = "Thane Krios";
     Temporary thane = Temporary(name, 0.5);
     EXPECT_EQ(thane.getType(), "[T]");
}

TEST(FulltimeTest, Vacation)
{
     std::string name = "Jane Shepard";
     Fulltime shepard = Fulltime(name, -1.0);

     EXPECT_EQ(shepard.getVacation(), 0);

     shepard.setLongevity(0);
     EXPECT_EQ(shepard.getVacation(), 0);

     shepard.setLongevity(0.8);
     EXPECT_EQ(shepard.getVacation(), 0);

     shepard.setLongevity(1.0);
     EXPECT_EQ(shepard.getVacation(), 5);

     shepard.setLongevity(2.5);
     EXPECT_EQ(shepard.getVacation(), 10);
}

TEST(ContractorTest, Vacation)
{
     std::string name = "Zaeed Massani";
     Contractor zaeed = Contractor(name, 1.0);
     EXPECT_EQ(zaeed.getVacation(), NULL);
}

TEST(TemporaryTest, Vacation)
{
     std::string name = "Thane Krios";
     Temporary thane = Temporary(name, 1.0);
     EXPECT_EQ(thane.getVacation(), NULL);
}

TEST(FulltimeTest, Screen)
{
     std::string name = "Jane Shepard";
     std::string expected = "Name: Jane Shepard, Duration: 3.0 years, Vacation Accrued: 15 days";
     Fulltime shepard = Fulltime(name, 3.0);
     EXPECT_EQ(screen(shepard), expected);
}

TEST(Contractor, Screen)
{
     std::string name = "Zaeed Massani";
     std::string expected = "Name: Zaeed Massani, Duration: 1.0 years, Vacation Accrued: None";
     Contractor zaeed = Contractor(name, 1.0);
     EXPECT_EQ(screen(zaeed), expected);
}

TEST(Temporary, Screen)
{
     std::string name = "Thane Krios";
     std::string expected = "Name: Thane Krios, Duration: 0.5 years, Vacation Accrued: None";
     Temporary thane = Temporary(name, 0.5);
     EXPECT_EQ(screen(thane), expected);
}