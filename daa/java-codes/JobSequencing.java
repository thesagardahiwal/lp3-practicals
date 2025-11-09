import java.util.*;

class Job {
    String id;
    int deadline;
    int profit;

    Job(String id, int deadline, int profit) {
        this.id = id;
        this.deadline = deadline;
        this.profit = profit;
    }
}

public class JobSequencing {
    public static void main(String[] args) {
        Job[] jobs = {
            new Job("a", 2, 100),
            new Job("b", 1, 19),
            new Job("c", 2, 27),
            new Job("d", 1, 25),
            new Job("e", 3, 15)
        };

        jobSequencing(jobs);
    }

    private static void jobSequencing(Job[] jobs) {
        Arrays.sort(jobs, (a, b) -> b.profit - a.profit);

        int maxDeadline = 0;
        for (Job job : jobs) {
            if (job.deadline > maxDeadline)
                maxDeadline = job.deadline;
        }

        String[] result = new String[maxDeadline];  
        boolean[] slot = new boolean[maxDeadline];  

        int totalProfit = 0;

        for (Job job : jobs) {
            for (int j = Math.min(maxDeadline, job.deadline) - 1; j >= 0; j--) {
                if (!slot[j]) {
                    slot[j] = true;
                    result[j] = job.id;
                    totalProfit += job.profit;
                    break;
                }
            }
        }

        System.out.print("Scheduled Jobs: ");
        for (String jobId : result) {
            if (jobId != null) System.out.print(jobId + " ");
        }
        System.out.println("\nTotal Profit: " + totalProfit);
    }
}
