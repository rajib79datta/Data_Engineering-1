import java.io.IOException;
import java.util.StringTokenizer;
import java.util.TreeMap;
import java.util.Map;
import java.util.regex.Pattern;
import java.util.ArrayList;
import java.io.BufferedReader;
import java.io.FileReader;


import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class WordCount {

  public static class TokenizerMapper
       extends Mapper<Object, Text, Text, IntWritable>{

    private final static IntWritable one = new IntWritable(1);
    private Text word = new Text();

    public void map(Object key, Text value, Context context
                    ) throws IOException, InterruptedException {
      StringTokenizer itr = new StringTokenizer(value.toString());
      while (itr.hasMoreTokens()) {
	String token = itr.nextToken();
	// Extract the first letter of the token and convert to lowercase
	if (token.length() > 0 && Character.isLetter(token.charAt(0))) {
	  char firstLetter = Character.toLowerCase(token.charAt(0));
	  if (firstLetter >= 'a' && firstLetter <= 'z') { // Check if the first letter is within 'a' to 'z'
           word.set(String.valueOf(firstLetter));
           context.write(word, one);
	}
      }
    }
  }
}
  public static class IntSumReducer
       extends Reducer<Text,IntWritable,Text,IntWritable> {
    private IntWritable result = new IntWritable();

    public void reduce(Text key, Iterable<IntWritable> values,
                       Context context
                       ) throws IOException, InterruptedException {
      int sum = 0;
      for (IntWritable val : values) {
        sum += val.get();
      }
      result.set(sum);
      context.write(key, result);
    }
  }

  public static void main(String[] args) throws Exception {
    Configuration conf = new Configuration();
    Job job = Job.getInstance(conf, "word count");
    job.setJarByClass(WordCount.class);
    job.setMapperClass(TokenizerMapper.class);
    job.setCombinerClass(IntSumReducer.class);
    job.setReducerClass(IntSumReducer.class);
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(IntWritable.class);
    FileInputFormat.addInputPath(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path(args[1]));
   // System.exit(job.waitForCompletion(true) ? 0 : 1);
   if(job.waitForCompletion(true)) {
        // Plotting the results
        TreeMap<String, Integer> counts = getLetterCounts(job);
        plotCounts(counts);
    } else {
        System.exit(1);
    }
 }

private static TreeMap<String, Integer> getLetterCounts(Job job) throws IOException {
    TreeMap<String, Integer> counts = new TreeMap<>();
    String outputPath = job.getConfiguration().get("mapreduce.output.fileoutputformat.outputdir");
    Path resultFile = new Path(outputPath + "/part-r-00000");
    try (BufferedReader br = new BufferedReader(new FileReader(resultFile.toString()))) {
        String line;
        while ((line = br.readLine()) != null) {
            String[] parts = line.split("\\s+");
            counts.put(parts[0], Integer.parseInt(parts[1]));
        }
    }
    return counts;
  }

  private static void plotCounts(TreeMap<String, Integer> counts) {
    // Your code for plotting the counts using JFreeChart or any other plotting library
    // Here is just a simple example using print statements
    System.out.println("Letter Counts:");
    for (Map.Entry<String, Integer> entry : counts.entrySet()) {
        System.out.println(entry.getKey() + ": " + entry.getValue());
    }
  }
}



