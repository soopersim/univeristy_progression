
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: W19314851
# Date: 24 November 2022


def histogram():
   print("Histogram \nProgress 1   : \nTrailer 1   :\nRetriever 2  :\nExcluded 1  : ")

def progression_check():
   while True:
      try:
         accepted_range = range(0, 140, 20)
         pass_credits = int(input("Please enter pass credits: "))
         if pass_credits not in accepted_range:
            print("Out of range ")
            continue
      except ValueError:
         print("Integer required ")
         continue
      else:
         try:
            defer_credits = int(input("Please enter defer credits: "))
            if defer_credits not in accepted_range:
               print("Out of range ")
               continue
         except ValueError:
            print("Integer required ")
            continue
         else:
            try:
               failed_credits = int(input("Please enter fail credits: "))
               if failed_credits not in accepted_range:
                  print("Out of range ")
            except ValueError:
               print("Integer required ")
               continue
            else:
               break

   if pass_credits == 120:
      print("Progress")
      input("Would you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ")
      if "y".lower():
         return progression_check()
   elif pass_credits + failed_credits + defer_credits != 120:
      print("Total incorrect ")
      input("Would you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ")
      if "y".lower():
         return progression_check()
      if "q".lower():
         print("Histogram \nProgress 1   : \nTrailer 1   :\nRetriever 2  :\nExcluded 1  : ")
   elif failed_credits >= 80 and pass_credits + defer_credits <= 40:
      print("Exclude")
      input("Would you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ")
      if "y".lower():
         return progression_check()
      if "q".lower():
         print("Histogram \nProgress 1   : \nTrailer 1   :\nRetriever 2  :\nExcluded 1  : ")
   elif pass_credits <= 80 and defer_credits + failed_credits <= 120:
      print("Do not progress - module retriever")
      input("Would you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ")
      if "y".lower():
         return progression_check()
      if "q".lower():
         print("Histogram \nProgress 1   : \nTrailer 1   :\nRetriever 2  :\nExcluded 1  : ")
   elif pass_credits == 100 and defer_credits + failed_credits == 20:
      print("Progress (module trailer) ")
      input("Would you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ")
      if "y".lower():
         return progression_check()
      if "q".lower():
         print("Histogram \nProgress 1   : \nTrailer 1   :\nRetriever 2  :\nExcluded 1  : ")

progression_check()