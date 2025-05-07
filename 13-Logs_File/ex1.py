users_log = dict()
last_user = ""

#with open("server_logs.log") as file:
    # for line in file:
    #     parts = line.split()  # Split by spaces
    #     date = parts[0]
    #     time = parts[1]
    #     level = parts[2]
    #
    #     message = " ".join(parts[3:])
    #     if "User" in message:
    #         #print(message.split())
    #         last_user = message.split()[1]
    #         if last_user not in users_log:
    #             users_log[last_user] = []
    #     if "User" in message:
    #         users_log[last_user].append(" ".join(message.split()[2:]))
    #     else:
    #         users_log[last_user].append(message)

        #print(f"date:{date}, Time: {time} ,Level: {level}, Message: {message}")

#print(open("crdownload").readline().strip())

#print(users_log)


# def count_log_level_error(filename):
#     error_count = 0
#     with open(filename, 'r') as file:
#         for line in file:
#             if line.split()[2] == 'ERROR':
#                 error_count += 1
#     return error_count
#
# filename = "crdownload"
# print(count_log_level_error(filename))

# def count_transactions(filename):
#     begun_transactions = set()
#     count = 0
#
#     with open(filename, 'r') as file:
#         for line in file:
#             if "transaction" in line:
#                 if "begun" in line :
#                     transaction_id = line.split('transaction')[1].split()[0]
#                     begun_transactions.add(transaction_id)
#                 elif "done" in line and "id" in line:
#                     transaction_id = line.split('id=')[1].split()[0]
#                     if transaction_id in begun_transactions:
#                         count += 1
#                         begun_transactions.remove(transaction_id)
#     return count
#
#
# filename = 'crdownload'
# transaction_count = count_transactions(filename)
# print(f"Total completed transactions: {transaction_count}")

#
# from datetime import datetime
#
#
# def find_fastest_transaction(filename):
#     begun_transactions = {}
#     fastest_transaction = None
#     fastest_time = float('inf')
#
#     with open(filename, 'r') as file:
#         for line in file:
#
#             if "transaction" in line and "begun" in line:
#                 parts = line.split("transaction")
#                 transaction_id = parts[1].split()[0]
#                 timestamp_str = line.split()[0] + " " + line.split()[1]  # Date and time together
#
#                 # Parse the timestamp
#                 start_time = datetime.strptime(timestamp_str, "%d-%m-%Y %H:%M:%S.%f")
#                 begun_transactions[transaction_id] = start_time
#
#             elif "transaction done" in line:
#                 if "id=" in line:
#                     parts = line.split("id=")
#                     transaction_id = parts[1].split()[0]
#                     timestamp_str = line.split()[0] + " " + line.split()[1]  # Date and time together
#
#                     # Parse the timestamp
#                     end_time = datetime.strptime(timestamp_str, "%d-%m-%Y %H:%M:%S.%f")
#
#                     if transaction_id in begun_transactions:
#                         start_time = begun_transactions.pop(transaction_id)
#                         # Calculate the time difference in milliseconds
#                         time_diff = (end_time - start_time).total_seconds() * 1000
#
#                         if time_diff < fastest_time:
#                             fastest_time = time_diff
#                             fastest_transaction = transaction_id
#
#     return fastest_transaction
#
#
# filename = 'crdownload'
# fastest_transaction= find_fastest_transaction(filename)
#
# if fastest_transaction:
#     print(f"The fastest transaction is ID {fastest_transaction}")


from datetime import datetime

def calculate_average_transaction_time(file_name):
    begun_transactions = {}
    total_time = 0
    transaction_count = 0

    with open(file_name, 'r') as file:
        for line in file:

            if "transaction" in line and "begun" in line:
                parts = line.split("transaction")
                transaction_id = parts[1].split()[0]
                timestamp_str = line.split()[0] + " " + line.split()[1]  # Date and time together

                start_time = datetime.strptime(timestamp_str, "%d-%m-%Y %H:%M:%S.%f")
                begun_transactions[transaction_id] = start_time

            elif "transaction done" in line:
                if "id=" in line:
                    parts = line.split("id=")
                    transaction_id = parts[1].split()[0]
                    timestamp_str = line.split()[0] + " " + line.split()[1]  # Date and time together

                    end_time = datetime.strptime(timestamp_str, "%d-%m-%Y %H:%M:%S.%f")

                    if transaction_id in begun_transactions:
                        start_time = begun_transactions.pop(transaction_id)
                        time_diff = (end_time - start_time).total_seconds() * 1000
                        total_time += time_diff
                        transaction_count += 1

    return total_time / transaction_count


file_name= 'crdownload'
average_time = calculate_average_transaction_time(file_name)

if average_time > 0:
    print(f"The average transaction time is {average_time:.2f} ms")
else:
    print("No valid transactions found.")

